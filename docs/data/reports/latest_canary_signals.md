# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T23:37:27.532176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.22` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0381` n `12`; crypto_alt avg `0.0331` n `228`; crypto_major avg `0.0246` n `8`; equity avg `0.0006` n `74`; fx avg `0.0166` n `6`; index avg `0.0495` n `23`; metal avg `0.0021` n `18`; unknown avg `0.0314` n `643`
- 1h: commodity avg `-0.1867` n `12`; crypto_alt avg `-0.2182` n `228`; crypto_major avg `-0.2656` n `8`; equity avg `0.0515` n `74`; fx avg `0.0396` n `6`; index avg `0.0844` n `23`; metal avg `0.062` n `18`; unknown avg `0.0938` n `643`
- 4h: commodity avg `-0.2961` n `12`; crypto_alt avg `-0.8361` n `228`; crypto_major avg `-0.996` n `8`; equity avg `0.111` n `74`; fx avg `0.0113` n `6`; index avg `0.224` n `23`; metal avg `0.1631` n `18`; unknown avg `0.6913` n `643`
- 24h: commodity avg `-0.4953` n `12`; crypto_alt avg `-0.5707` n `228`; crypto_major avg `-0.3589` n `8`; equity avg `-0.5423` n `74`; fx avg `0.0242` n `6`; index avg `0.4058` n `23`; metal avg `0.2619` n `18`; unknown avg `41.1553` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
