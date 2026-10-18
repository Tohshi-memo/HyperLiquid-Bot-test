# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T21:07:29.456219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0026` n `13`; crypto_alt avg `0.0708` n `237`; crypto_major avg `0.1571` n `8`; equity avg `-0.0028` n `151`; fx avg `-0.0322` n `6`; index avg `0.0057` n `26`; metal avg `0.0058` n `20`; unknown avg `1.2839` n `1186`
- 1h: commodity avg `-0.0008` n `13`; crypto_alt avg `0.0268` n `237`; crypto_major avg `0.1647` n `8`; equity avg `0.0205` n `151`; fx avg `-0.0072` n `6`; index avg `0.0068` n `26`; metal avg `-0.0038` n `20`; unknown avg `7.6536` n `1186`
- 4h: commodity avg `0.0319` n `13`; crypto_alt avg `-1.8817` n `237`; crypto_major avg `-0.7438` n `8`; equity avg `-0.3312` n `151`; fx avg `-0.0383` n `6`; index avg `-0.0512` n `26`; metal avg `-0.0439` n `20`; unknown avg `2.935` n `1152`
- 24h: commodity avg `0.0555` n `13`; crypto_alt avg `-5.2776` n `236`; crypto_major avg `-2.4059` n `8`; equity avg `-1.2425` n `151`; fx avg `-0.0469` n `6`; index avg `-0.157` n `26`; metal avg `-0.0912` n `20`; unknown avg `1.5599` n `1007`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2102`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.144`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1395`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.12`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0765`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
