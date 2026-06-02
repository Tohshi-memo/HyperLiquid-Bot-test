# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T06:22:28.994966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.73` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.803` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.613` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.0232` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0141` n `12`; crypto_alt avg `-0.2883` n `228`; crypto_major avg `-0.258` n `8`; equity avg `0.0749` n `69`; fx avg `0.0355` n `6`; index avg `0.0122` n `23`; metal avg `0.0753` n `18`; unknown avg `-0.4297` n `422`
- 1h: commodity avg `-0.0155` n `12`; crypto_alt avg `-0.9839` n `228`; crypto_major avg `-0.7827` n `8`; equity avg `0.086` n `69`; fx avg `0.0419` n `6`; index avg `0.1586` n `23`; metal avg `0.5448` n `18`; unknown avg `-0.2299` n `412`
- 4h: commodity avg `-0.351` n `12`; crypto_alt avg `-0.1165` n `228`; crypto_major avg `-0.5963` n `8`; equity avg `1.0167` n `69`; fx avg `0.0594` n `6`; index avg `0.4269` n `23`; metal avg `1.2067` n `18`; unknown avg `-0.154` n `412`
- 24h: commodity avg `-1.0167` n `12`; crypto_alt avg `-0.7708` n `228`; crypto_major avg `-1.8277` n `8`; equity avg `0.0545` n `69`; fx avg `0.1498` n `6`; index avg `-0.3042` n `23`; metal avg `1.0714` n `18`; unknown avg `1.8313` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
