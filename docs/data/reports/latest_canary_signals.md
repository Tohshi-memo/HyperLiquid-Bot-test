# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T20:35:22.291363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0176` n `12`; crypto_alt avg `-0.1114` n `230`; crypto_major avg `-0.1886` n `8`; equity avg `-0.0101` n `96`; fx avg `-0.0029` n `6`; index avg `0.0009` n `25`; metal avg `0.0017` n `20`; unknown avg `0.0035` n `770`
- 1h: commodity avg `-0.076` n `12`; crypto_alt avg `0.1212` n `230`; crypto_major avg `0.0892` n `8`; equity avg `-0.0299` n `96`; fx avg `0.0091` n `6`; index avg `-0.0083` n `25`; metal avg `-0.0017` n `20`; unknown avg `-0.0009` n `770`
- 4h: commodity avg `0.16` n `12`; crypto_alt avg `0.3152` n `230`; crypto_major avg `0.4762` n `8`; equity avg `0.0021` n `96`; fx avg `-0.021` n `6`; index avg `-0.0237` n `25`; metal avg `-0.0179` n `20`; unknown avg `0.1315` n `770`
- 24h: commodity avg `0.3357` n `12`; crypto_alt avg `-0.3118` n `230`; crypto_major avg `0.447` n `8`; equity avg `-0.2467` n `96`; fx avg `-0.0969` n `6`; index avg `0.0372` n `25`; metal avg `0.0252` n `20`; unknown avg `-0.0027` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
