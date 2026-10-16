# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T19:22:30.509360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `13`; crypto_alt avg `0.6305` n `236`; crypto_major avg `0.5693` n `8`; equity avg `0.5347` n `151`; fx avg `0.0061` n `6`; index avg `0.087` n `26`; metal avg `0.0442` n `20`; unknown avg `5.6125` n `1177`
- 1h: commodity avg `-0.0346` n `13`; crypto_alt avg `-0.0699` n `236`; crypto_major avg `-0.1582` n `8`; equity avg `-0.138` n `151`; fx avg `0.0053` n `6`; index avg `-0.0086` n `26`; metal avg `0.0262` n `20`; unknown avg `85.5333` n `1175`
- 4h: commodity avg `0.7369` n `13`; crypto_alt avg `-0.7518` n `236`; crypto_major avg `-0.3299` n `8`; equity avg `-1.118` n `151`; fx avg `-0.0121` n `6`; index avg `-0.2512` n `26`; metal avg `-0.1628` n `20`; unknown avg `1.7282` n `1140`
- 24h: commodity avg `0.3313` n `13`; crypto_alt avg `-2.2548` n `236`; crypto_major avg `-2.0232` n `8`; equity avg `-3.6471` n `151`; fx avg `0.008` n `6`; index avg `-0.6391` n `26`; metal avg `-0.0544` n `20`; unknown avg `-0.3488` n `904`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1582`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1111`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0871`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0742`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0725`, n `666`, weak_sample_signal
