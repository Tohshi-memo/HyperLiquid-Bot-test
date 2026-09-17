# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T21:07:31.565888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `12`; crypto_alt avg `-0.1645` n `234`; crypto_major avg `-0.0828` n `8`; equity avg `0.0134` n `140`; fx avg `-0.01` n `6`; index avg `0.0003` n `26`; metal avg `0.024` n `20`; unknown avg `0.6862` n `895`
- 1h: commodity avg `0.0183` n `12`; crypto_alt avg `-0.0508` n `234`; crypto_major avg `-0.1178` n `8`; equity avg `-0.003` n `140`; fx avg `-0.0112` n `6`; index avg `-0.0102` n `26`; metal avg `-0.0048` n `20`; unknown avg `20.7691` n `889`
- 4h: commodity avg `-0.2177` n `12`; crypto_alt avg `-0.2822` n `234`; crypto_major avg `-0.2959` n `8`; equity avg `-0.1026` n `140`; fx avg `-0.0142` n `6`; index avg `-0.0423` n `26`; metal avg `-0.2259` n `20`; unknown avg `4.6935` n `865`
- 24h: commodity avg `-0.2125` n `12`; crypto_alt avg `3.739` n `234`; crypto_major avg `1.6852` n `8`; equity avg `2.4062` n `138`; fx avg `-0.0115` n `6`; index avg `0.441` n `26`; metal avg `0.5554` n `20`; unknown avg `5.9975` n `771`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
