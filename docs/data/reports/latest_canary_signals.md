# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T06:37:33.903359+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0138` n `13`; crypto_alt avg `0.1788` n `239`; crypto_major avg `0.0787` n `8`; equity avg `0.2159` n `158`; fx avg `0.0178` n `6`; index avg `0.0315` n `27`; metal avg `-0.0474` n `20`; unknown avg `158.5393` n `1262`
- 1h: commodity avg `0.0967` n `13`; crypto_alt avg `0.7746` n `239`; crypto_major avg `0.2927` n `8`; equity avg `1.0678` n `158`; fx avg `0.0449` n `6`; index avg `0.0824` n `27`; metal avg `0.389` n `20`; unknown avg `0.2963` n `1240`
- 4h: commodity avg `0.3353` n `13`; crypto_alt avg `2.3064` n `239`; crypto_major avg `1.6405` n `8`; equity avg `2.6485` n `158`; fx avg `0.0758` n `6`; index avg `0.4306` n `27`; metal avg `0.8354` n `20`; unknown avg `1.1521` n `1234`
- 24h: commodity avg `-0.0499` n `13`; crypto_alt avg `2.4507` n `239`; crypto_major avg `1.2118` n `8`; equity avg `2.3833` n `158`; fx avg `0.1473` n `6`; index avg `0.0993` n `27`; metal avg `0.651` n `20`; unknown avg `190.3742` n `1051`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2233`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
