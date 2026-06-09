# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T21:37:23.960057+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0312` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0354` n `12`; crypto_alt avg `-0.0742` n `228`; crypto_major avg `-0.1284` n `8`; equity avg `-0.1462` n `74`; fx avg `-0.0906` n `6`; index avg `-0.1233` n `23`; metal avg `-0.0504` n `18`; unknown avg `-0.077` n `547`
- 1h: commodity avg `0.205` n `12`; crypto_alt avg `-0.4997` n `228`; crypto_major avg `-0.4291` n `8`; equity avg `-0.4402` n `74`; fx avg `-0.055` n `6`; index avg `-0.2345` n `23`; metal avg `-0.0113` n `18`; unknown avg `-0.1976` n `547`
- 4h: commodity avg `0.3642` n `12`; crypto_alt avg `-0.0166` n `228`; crypto_major avg `-0.0797` n `8`; equity avg `0.5549` n `74`; fx avg `-0.1171` n `6`; index avg `0.9515` n `23`; metal avg `0.1564` n `18`; unknown avg `-0.0237` n `547`
- 24h: commodity avg `-0.7488` n `12`; crypto_alt avg `-2.5834` n `228`; crypto_major avg `-3.5938` n `8`; equity avg `-2.1791` n `74`; fx avg `0.0938` n `6`; index avg `-0.9186` n `23`; metal avg `-1.5969` n `18`; unknown avg `-1.2778` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0498`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0443`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0423`, n `668`, weak_sample_signal
