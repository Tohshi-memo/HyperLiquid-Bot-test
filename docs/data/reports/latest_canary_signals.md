# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T22:37:31.297388+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0995` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0882` n `12`; crypto_alt avg `-0.3042` n `228`; crypto_major avg `-0.3062` n `8`; equity avg `-0.0733` n `78`; fx avg `0.0135` n `6`; index avg `-0.0104` n `23`; metal avg `0.0085` n `18`; unknown avg `-0.1244` n `702`
- 1h: commodity avg `-0.2466` n `12`; crypto_alt avg `-0.5057` n `228`; crypto_major avg `-0.5382` n `8`; equity avg `-0.2623` n `78`; fx avg `0.045` n `6`; index avg `-0.0799` n `23`; metal avg `-0.0219` n `18`; unknown avg `0.4118` n `702`
- 4h: commodity avg `-0.1214` n `12`; crypto_alt avg `-1.416` n `228`; crypto_major avg `-1.1757` n `8`; equity avg `-0.3167` n `78`; fx avg `-0.0525` n `6`; index avg `-0.0762` n `23`; metal avg `-0.0704` n `18`; unknown avg `1.0971` n `694`
- 24h: commodity avg `0.0958` n `12`; crypto_alt avg `-0.563` n `228`; crypto_major avg `-1.6917` n `8`; equity avg `-0.1889` n `78`; fx avg `-0.1247` n `6`; index avg `-0.1091` n `23`; metal avg `-0.1976` n `18`; unknown avg `1.0678` n `645`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
