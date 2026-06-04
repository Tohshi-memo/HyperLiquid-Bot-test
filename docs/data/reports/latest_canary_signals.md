# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T21:52:22.474461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3165` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.2537` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.2155` n `12`; crypto_alt avg `-0.1068` n `228`; crypto_major avg `0.0232` n `8`; equity avg `-0.0188` n `74`; fx avg `-0.0023` n `6`; index avg `0.1073` n `23`; metal avg `-0.0155` n `18`; unknown avg `-0.076` n `424`
- 1h: commodity avg `-0.0259` n `12`; crypto_alt avg `-1.522` n `228`; crypto_major avg `-1.0297` n `8`; equity avg `-0.0366` n `74`; fx avg `0.008` n `6`; index avg `0.224` n `23`; metal avg `-0.0458` n `18`; unknown avg `0.5058` n `424`
- 4h: commodity avg `0.2083` n `12`; crypto_alt avg `-2.3641` n `228`; crypto_major avg `-1.365` n `8`; equity avg `-0.9257` n `74`; fx avg `-0.0178` n `6`; index avg `-0.0485` n `23`; metal avg `-0.1646` n `18`; unknown avg `-0.3183` n `424`
- 24h: commodity avg `-0.9328` n `12`; crypto_alt avg `-7.7802` n `228`; crypto_major avg `-5.3966` n `8`; equity avg `-0.398` n `73`; fx avg `0.0558` n `6`; index avg `0.4226` n `23`; metal avg `0.7589` n `18`; unknown avg `0.203` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
