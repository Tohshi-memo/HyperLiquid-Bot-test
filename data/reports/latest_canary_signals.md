# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T03:37:15.179847+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3099` n `12`; crypto_alt avg `0.0542` n `228`; crypto_major avg `-0.0222` n `8`; equity avg `0.0252` n `67`; fx avg `0.0049` n `6`; index avg `-0.1981` n `23`; metal avg `0.0094` n `18`; unknown avg `0.069` n `397`
- 1h: commodity avg `-0.5904` n `12`; crypto_alt avg `-0.0639` n `228`; crypto_major avg `-0.133` n `8`; equity avg `0.1941` n `67`; fx avg `-0.0218` n `6`; index avg `-0.1328` n `23`; metal avg `-0.0472` n `18`; unknown avg `-0.1054` n `396`
- 4h: commodity avg `-0.513` n `12`; crypto_alt avg `0.2483` n `228`; crypto_major avg `-0.5343` n `8`; equity avg `0.3392` n `67`; fx avg `-0.1684` n `6`; index avg `0.0265` n `23`; metal avg `-0.5138` n `18`; unknown avg `-0.0536` n `396`
- 24h: commodity avg `-0.1628` n `12`; crypto_alt avg `-1.0011` n `228`; crypto_major avg `-0.3337` n `8`; equity avg `0.396` n `67`; fx avg `-0.0549` n `6`; index avg `-0.4025` n `23`; metal avg `0.4718` n `18`; unknown avg `-0.5844` n `386`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
