# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T18:52:19.458648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7731` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1428` n `12`; crypto_alt avg `-0.1155` n `228`; crypto_major avg `-0.0011` n `8`; equity avg `-0.0817` n `67`; fx avg `-0.0091` n `6`; index avg `0.0062` n `23`; metal avg `0.0966` n `18`; unknown avg `0.2057` n `418`
- 1h: commodity avg `-0.2744` n `12`; crypto_alt avg `-0.2278` n `228`; crypto_major avg `-0.004` n `8`; equity avg `-0.0809` n `67`; fx avg `-0.0028` n `6`; index avg `0.0791` n `23`; metal avg `0.1631` n `18`; unknown avg `-0.0172` n `418`
- 4h: commodity avg `-0.4983` n `12`; crypto_alt avg `-2.1006` n `228`; crypto_major avg `-1.6611` n `8`; equity avg `-0.2292` n `67`; fx avg `0.0306` n `6`; index avg `0.112` n `23`; metal avg `-0.1662` n `18`; unknown avg `0.228` n `418`
- 24h: commodity avg `0.4392` n `12`; crypto_alt avg `-2.527` n `228`; crypto_major avg `-1.5605` n `8`; equity avg `-0.4261` n `67`; fx avg `-0.1223` n `6`; index avg `0.4506` n `23`; metal avg `-1.2297` n `18`; unknown avg `-0.3735` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.176`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
