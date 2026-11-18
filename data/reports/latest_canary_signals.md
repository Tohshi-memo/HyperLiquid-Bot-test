# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T11:52:28.005252+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0503` n `13`; crypto_alt avg `0.0528` n `239`; crypto_major avg `-0.0704` n `8`; equity avg `-0.0481` n `163`; fx avg `-0.004` n `6`; index avg `-0.0179` n `27`; metal avg `-0.033` n `20`; unknown avg `0.2699` n `1266`
- 1h: commodity avg `0.2009` n `13`; crypto_alt avg `-0.1233` n `239`; crypto_major avg `-0.3704` n `8`; equity avg `-0.3377` n `163`; fx avg `-0.0136` n `6`; index avg `-0.0675` n `27`; metal avg `-0.076` n `20`; unknown avg `0.2472` n `1264`
- 4h: commodity avg `0.2431` n `13`; crypto_alt avg `-0.0423` n `239`; crypto_major avg `-0.8` n `8`; equity avg `-0.3075` n `163`; fx avg `-0.0089` n `6`; index avg `-0.0272` n `27`; metal avg `-0.1868` n `20`; unknown avg `102.3794` n `1186`
- 24h: commodity avg `-0.0944` n `13`; crypto_alt avg `0.0149` n `239`; crypto_major avg `0.0038` n `8`; equity avg `0.1079` n `163`; fx avg `-0.109` n `6`; index avg `-0.0182` n `27`; metal avg `-1.1666` n `20`; unknown avg `6.0148` n `1099`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
