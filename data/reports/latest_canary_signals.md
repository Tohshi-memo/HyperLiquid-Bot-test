# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T08:22:27.283083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.69` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-2.4083` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.1182` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.9545` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1277` n `12`; crypto_alt avg `-0.0019` n `228`; crypto_major avg `-0.0648` n `8`; equity avg `0.0871` n `69`; fx avg `-0.0198` n `6`; index avg `0.0717` n `23`; metal avg `-0.0478` n `18`; unknown avg `-0.2331` n `422`
- 1h: commodity avg `-0.1213` n `12`; crypto_alt avg `0.0481` n `228`; crypto_major avg `-0.2992` n `8`; equity avg `0.2771` n `69`; fx avg `-0.0028` n `6`; index avg `0.122` n `23`; metal avg `0.0366` n `18`; unknown avg `-0.1673` n `422`
- 4h: commodity avg `-0.1963` n `12`; crypto_alt avg `-1.0472` n `228`; crypto_major avg `-1.3946` n `8`; equity avg `0.7236` n `69`; fx avg `0.0298` n `6`; index avg `0.5599` n `23`; metal avg `1.0137` n `18`; unknown avg `-0.9034` n `412`
- 24h: commodity avg `-1.3292` n `12`; crypto_alt avg `0.161` n `228`; crypto_major avg `-1.3304` n `8`; equity avg `0.7304` n `69`; fx avg `0.1247` n `6`; index avg `0.029` n `23`; metal avg `1.4908` n `18`; unknown avg `1.1623` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1909`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
