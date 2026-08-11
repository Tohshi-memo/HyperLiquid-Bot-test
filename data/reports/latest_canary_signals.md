# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T03:52:27.891870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0249` n `12`; crypto_alt avg `0.0067` n `230`; crypto_major avg `-0.053` n `8`; equity avg `0.1121` n `113`; fx avg `-0.0001` n `6`; index avg `0.0067` n `25`; metal avg `-0.015` n `20`; unknown avg `1.2912` n `785`
- 1h: commodity avg `-0.0404` n `12`; crypto_alt avg `0.0191` n `230`; crypto_major avg `0.0352` n `8`; equity avg `0.0854` n `113`; fx avg `-0.0019` n `6`; index avg `0.0251` n `25`; metal avg `0.0454` n `20`; unknown avg `1.333` n `785`
- 4h: commodity avg `0.007` n `12`; crypto_alt avg `0.1919` n `230`; crypto_major avg `0.2459` n `8`; equity avg `0.6919` n `113`; fx avg `-0.0382` n `6`; index avg `0.1677` n `25`; metal avg `0.1125` n `20`; unknown avg `-0.1116` n `785`
- 24h: commodity avg `0.7816` n `12`; crypto_alt avg `-0.529` n `230`; crypto_major avg `-0.4646` n `8`; equity avg `-0.9284` n `113`; fx avg `0.1236` n `6`; index avg `0.0551` n `25`; metal avg `0.5389` n `20`; unknown avg `103.8872` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1596`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.159`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1576`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1559`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1546`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.141`, n `669`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1236`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1192`, n `669`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1076`, n `669`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0953`, n `669`, weak_sample_signal
