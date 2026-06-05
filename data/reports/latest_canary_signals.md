# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T07:52:21.200898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `1.6086` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.0049` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0126` n `12`; crypto_alt avg `0.3115` n `228`; crypto_major avg `0.3335` n `8`; equity avg `0.0375` n `74`; fx avg `0.0061` n `6`; index avg `0.1185` n `23`; metal avg `-0.0047` n `18`; unknown avg `0.1202` n `424`
- 1h: commodity avg `-0.2891` n `12`; crypto_alt avg `1.5695` n `228`; crypto_major avg `1.681` n `8`; equity avg `0.2247` n `74`; fx avg `0.048` n `6`; index avg `0.0566` n `23`; metal avg `0.0724` n `18`; unknown avg `1.2178` n `424`
- 4h: commodity avg `-0.387` n `12`; crypto_alt avg `-1.3793` n `228`; crypto_major avg `-0.8708` n `8`; equity avg `-0.0619` n `74`; fx avg `0.0023` n `6`; index avg `0.1341` n `23`; metal avg `0.2266` n `18`; unknown avg `0.1004` n `404`
- 24h: commodity avg `-0.6505` n `12`; crypto_alt avg `-5.4945` n `228`; crypto_major avg `-3.8377` n `8`; equity avg `-1.6882` n `73`; fx avg `0.1227` n `6`; index avg `-0.5178` n `23`; metal avg `-0.2238` n `18`; unknown avg `0.296` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
