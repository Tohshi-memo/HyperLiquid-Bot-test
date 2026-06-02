# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T09:07:27.172183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.69` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.5837` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4418` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0953` n `12`; crypto_alt avg `-0.0011` n `228`; crypto_major avg `-0.0484` n `8`; equity avg `-0.169` n `69`; fx avg `-0.0132` n `6`; index avg `-0.0349` n `23`; metal avg `-0.0306` n `18`; unknown avg `-0.0301` n `422`
- 1h: commodity avg `-0.0919` n `12`; crypto_alt avg `-0.1316` n `228`; crypto_major avg `-0.2564` n `8`; equity avg `-0.097` n `69`; fx avg `-0.0368` n `6`; index avg `0.0701` n `23`; metal avg `-0.2995` n `18`; unknown avg `-0.3215` n `422`
- 4h: commodity avg `-0.1516` n `12`; crypto_alt avg `-0.6141` n `228`; crypto_major avg `-1.0509` n `8`; equity avg `0.2981` n `69`; fx avg `0.038` n `6`; index avg `0.3909` n `23`; metal avg `0.5328` n `18`; unknown avg `-0.6553` n `412`
- 24h: commodity avg `-1.2179` n `12`; crypto_alt avg `-0.2408` n `228`; crypto_major avg `-1.7056` n `8`; equity avg `0.4309` n `69`; fx avg `0.1073` n `6`; index avg `-0.0088` n `23`; metal avg `1.0636` n `18`; unknown avg `0.9833` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
