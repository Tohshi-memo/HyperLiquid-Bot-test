# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T14:37:25.931050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0338` n `12`; crypto_alt avg `0.0913` n `230`; crypto_major avg `0.0355` n `8`; equity avg `0.028` n `96`; fx avg `-0.0098` n `6`; index avg `0.0181` n `25`; metal avg `-0.0555` n `20`; unknown avg `0.1105` n `769`
- 1h: commodity avg `0.0167` n `12`; crypto_alt avg `1.1942` n `230`; crypto_major avg `1.1445` n `8`; equity avg `2.4662` n `96`; fx avg `-0.0061` n `6`; index avg `0.3312` n `25`; metal avg `0.2037` n `20`; unknown avg `0.3202` n `769`
- 4h: commodity avg `0.2924` n `12`; crypto_alt avg `-0.0719` n `230`; crypto_major avg `-0.205` n `8`; equity avg `0.5889` n `96`; fx avg `0.0034` n `6`; index avg `0.057` n `25`; metal avg `-0.0282` n `20`; unknown avg `0.2628` n `769`
- 24h: commodity avg `0.2959` n `12`; crypto_alt avg `-2.0219` n `230`; crypto_major avg `-3.1735` n `8`; equity avg `-2.8067` n `94`; fx avg `-0.0496` n `6`; index avg `-0.4989` n `25`; metal avg `-0.4954` n `20`; unknown avg `-0.3748` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
