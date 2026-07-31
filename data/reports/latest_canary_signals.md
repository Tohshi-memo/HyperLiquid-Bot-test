# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T18:07:33.085939+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0204` n `12`; crypto_alt avg `-0.0125` n `230`; crypto_major avg `-0.0522` n `8`; equity avg `-0.0397` n `102`; fx avg `0.0491` n `6`; index avg `-0.0057` n `25`; metal avg `-0.0029` n `20`; unknown avg `-0.1118` n `780`
- 1h: commodity avg `0.0839` n `12`; crypto_alt avg `0.4257` n `230`; crypto_major avg `0.4087` n `8`; equity avg `0.4511` n `102`; fx avg `-0.0028` n `6`; index avg `0.0423` n `25`; metal avg `0.1311` n `20`; unknown avg `0.0957` n `780`
- 4h: commodity avg `-0.0402` n `12`; crypto_alt avg `1.2679` n `230`; crypto_major avg `0.4051` n `8`; equity avg `0.9835` n `102`; fx avg `0.1687` n `6`; index avg `0.2355` n `25`; metal avg `0.3568` n `20`; unknown avg `0.1455` n `780`
- 24h: commodity avg `0.1182` n `12`; crypto_alt avg `-0.1556` n `230`; crypto_major avg `-1.6928` n `8`; equity avg `0.8515` n `102`; fx avg `0.2308` n `6`; index avg `0.3347` n `25`; metal avg `-0.2649` n `20`; unknown avg `0.4153` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
