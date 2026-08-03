# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T02:07:22.016110+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0883` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0332` n `12`; crypto_alt avg `-0.0699` n `230`; crypto_major avg `-0.0586` n `8`; equity avg `0.1702` n `102`; fx avg `-0.0048` n `6`; index avg `0.0556` n `25`; metal avg `0.0095` n `20`; unknown avg `-0.1332` n `784`
- 1h: commodity avg `-0.1003` n `12`; crypto_alt avg `-0.2234` n `230`; crypto_major avg `-0.2332` n `8`; equity avg `0.0945` n `102`; fx avg `0.029` n `6`; index avg `0.076` n `25`; metal avg `0.0256` n `20`; unknown avg `-0.1971` n `784`
- 4h: commodity avg `0.2201` n `12`; crypto_alt avg `-0.9896` n `230`; crypto_major avg `-1.0943` n `8`; equity avg `0.4027` n `102`; fx avg `-0.2813` n `6`; index avg `-0.006` n `25`; metal avg `-0.1264` n `20`; unknown avg `0.2672` n `783`
- 24h: commodity avg `-0.627` n `12`; crypto_alt avg `-0.5437` n `230`; crypto_major avg `-0.1371` n `8`; equity avg `1.4548` n `102`; fx avg `-0.2753` n `6`; index avg `0.2249` n `25`; metal avg `0.094` n `20`; unknown avg `1.3548` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
