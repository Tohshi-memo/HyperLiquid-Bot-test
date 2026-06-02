# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T08:52:25.355258+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.63` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.9883` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.856` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.8442` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1287` n `12`; crypto_alt avg `-0.1877` n `228`; crypto_major avg `-0.2611` n `8`; equity avg `0.0155` n `69`; fx avg `-0.0087` n `6`; index avg `-0.0196` n `23`; metal avg `-0.1038` n `18`; unknown avg `-0.2693` n `422`
- 1h: commodity avg `-0.2082` n `12`; crypto_alt avg `-0.2596` n `228`; crypto_major avg `-0.3695` n `8`; equity avg `0.1858` n `69`; fx avg `-0.0173` n `6`; index avg `0.1394` n `23`; metal avg `-0.1694` n `18`; unknown avg `-0.3382` n `422`
- 4h: commodity avg `-0.2564` n `12`; crypto_alt avg `-0.9546` n `228`; crypto_major avg `-1.3367` n `8`; equity avg `0.5193` n `69`; fx avg `0.055` n `6`; index avg `0.5075` n `23`; metal avg `0.6516` n `18`; unknown avg `-0.5348` n `412`
- 24h: commodity avg `-1.3393` n `12`; crypto_alt avg `0.057` n `228`; crypto_major avg `-1.371` n `8`; equity avg `0.7493` n `69`; fx avg `0.1281` n `6`; index avg `0.0686` n `23`; metal avg `1.1167` n `18`; unknown avg `1.2397` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
