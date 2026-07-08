# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T22:07:27.940474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0347` n `12`; crypto_alt avg `0.2985` n `229`; crypto_major avg `0.1901` n `8`; equity avg `-0.0053` n `91`; fx avg `0.0127` n `6`; index avg `0.0117` n `25`; metal avg `0.0374` n `20`; unknown avg `0.0485` n `764`
- 1h: commodity avg `-0.0667` n `12`; crypto_alt avg `0.5361` n `229`; crypto_major avg `0.3597` n `8`; equity avg `0.2155` n `91`; fx avg `0.0213` n `6`; index avg `0.0136` n `25`; metal avg `0.0357` n `20`; unknown avg `0.0677` n `764`
- 4h: commodity avg `0.1962` n `12`; crypto_alt avg `0.1829` n `229`; crypto_major avg `0.1481` n `8`; equity avg `0.6083` n `91`; fx avg `-0.0092` n `6`; index avg `0.0332` n `25`; metal avg `0.0602` n `20`; unknown avg `0.987` n `764`
- 24h: commodity avg `0.3839` n `12`; crypto_alt avg `-1.2821` n `229`; crypto_major avg `-2.028` n `8`; equity avg `1.4549` n `91`; fx avg `0.0393` n `6`; index avg `-0.0202` n `25`; metal avg `-0.7` n `20`; unknown avg `0.0602` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
