# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T13:12:04.996516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.091` n `12`; crypto_alt avg `0.0545` n `230`; crypto_major avg `0.0652` n `8`; equity avg `0.0853` n `114`; fx avg `0.0189` n `6`; index avg `0.0188` n `25`; metal avg `0.0256` n `20`; unknown avg `0.0671` n `792`
- 1h: commodity avg `0.0576` n `12`; crypto_alt avg `-0.0611` n `230`; crypto_major avg `-0.191` n `8`; equity avg `-0.1671` n `114`; fx avg `0.0198` n `6`; index avg `-0.0205` n `25`; metal avg `-0.0132` n `20`; unknown avg `0.0152` n `792`
- 4h: commodity avg `0.026` n `12`; crypto_alt avg `0.1054` n `230`; crypto_major avg `0.0595` n `8`; equity avg `-0.3214` n `114`; fx avg `0.0368` n `6`; index avg `-0.0259` n `25`; metal avg `-0.0333` n `20`; unknown avg `1.6505` n `792`
- 24h: commodity avg `-0.0728` n `12`; crypto_alt avg `-0.1886` n `230`; crypto_major avg `0.6004` n `8`; equity avg `1.0079` n `114`; fx avg `0.0068` n `6`; index avg `0.1115` n `25`; metal avg `0.1177` n `20`; unknown avg `0.0156` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1671`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
