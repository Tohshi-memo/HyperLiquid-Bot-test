# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T06:07:30.419917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.3026` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.2818` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.2745` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.0313` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0087` n `12`; crypto_alt avg `-0.2316` n `230`; crypto_major avg `-0.2795` n `8`; equity avg `-0.0682` n `121`; fx avg `0.0068` n `6`; index avg `-0.0118` n `25`; metal avg `-0.0166` n `20`; unknown avg `-0.0187` n `778`
- 1h: commodity avg `-0.0107` n `12`; crypto_alt avg `-0.1668` n `230`; crypto_major avg `-0.4594` n `8`; equity avg `-0.1619` n `121`; fx avg `-0.0191` n `6`; index avg `-0.0216` n `25`; metal avg `-0.0084` n `20`; unknown avg `0.1002` n `778`
- 4h: commodity avg `-0.047` n `12`; crypto_alt avg `-2.3937` n `230`; crypto_major avg `-2.3215` n `8`; equity avg `-0.2902` n `121`; fx avg `-0.0109` n `6`; index avg `-0.0189` n `25`; metal avg `-0.0397` n `20`; unknown avg `-0.0347` n `778`
- 24h: commodity avg `-0.0469` n `12`; crypto_alt avg `-4.245` n `230`; crypto_major avg `-2.2197` n `8`; equity avg `-0.0827` n `121`; fx avg `0.0677` n `6`; index avg `-0.0105` n `25`; metal avg `0.0658` n `20`; unknown avg `3.3321` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
