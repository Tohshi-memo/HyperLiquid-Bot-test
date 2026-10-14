# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T16:22:34.914399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.406` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0476` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.714` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0343` n `13`; crypto_alt avg `-0.2254` n `235`; crypto_major avg `-0.305` n `8`; equity avg `-0.3944` n `151`; fx avg `-0.0293` n `6`; index avg `-0.0651` n `26`; metal avg `-0.0034` n `20`; unknown avg `2.1268` n `1137`
- 1h: commodity avg `0.051` n `13`; crypto_alt avg `-0.4846` n `235`; crypto_major avg `-0.7165` n `8`; equity avg `-0.9465` n `151`; fx avg `-0.0174` n `6`; index avg `-0.1499` n `26`; metal avg `-0.1137` n `20`; unknown avg `1.1523` n `1129`
- 4h: commodity avg `-0.1336` n `13`; crypto_alt avg `-2.541` n `235`; crypto_major avg `-2.5396` n `8`; equity avg `-3.1709` n `151`; fx avg `-0.1611` n `6`; index avg `-0.492` n `26`; metal avg `-0.8256` n `20`; unknown avg `5.2826` n `1102`
- 24h: commodity avg `0.0514` n `13`; crypto_alt avg `-3.0665` n `235`; crypto_major avg `-2.5591` n `8`; equity avg `-3.5155` n `151`; fx avg `-0.1729` n `6`; index avg `-0.4601` n `26`; metal avg `-0.8216` n `20`; unknown avg `1262.2526` n `981`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0954`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0807`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0723`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0692`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0507`, n `666`, weak_sample_signal
