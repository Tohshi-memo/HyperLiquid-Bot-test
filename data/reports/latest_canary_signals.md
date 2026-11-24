# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T03:22:28.071911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4697` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0737` n `13`; crypto_alt avg `0.3743` n `239`; crypto_major avg `0.2943` n `8`; equity avg `0.0941` n `166`; fx avg `0.0113` n `6`; index avg `0.0233` n `27`; metal avg `-0.0398` n `20`; unknown avg `0.0302` n `1264`
- 1h: commodity avg `0.0172` n `13`; crypto_alt avg `-0.8516` n `239`; crypto_major avg `-0.9667` n `8`; equity avg `-0.5372` n `166`; fx avg `-0.0079` n `6`; index avg `-0.027` n `27`; metal avg `-0.2702` n `20`; unknown avg `316.321` n `1262`
- 4h: commodity avg `-0.0781` n `13`; crypto_alt avg `-0.715` n `239`; crypto_major avg `-1.4319` n `8`; equity avg `-0.9506` n `166`; fx avg `0.0379` n `6`; index avg `0.0378` n `27`; metal avg `-0.2581` n `20`; unknown avg `398.4783` n `1256`
- 24h: commodity avg `-1.1839` n `13`; crypto_alt avg `-0.5137` n `239`; crypto_major avg `-1.2904` n `8`; equity avg `4.3686` n `166`; fx avg `-0.2272` n `6`; index avg `0.563` n `27`; metal avg `0.0366` n `20`; unknown avg `286.6296` n `1050`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
