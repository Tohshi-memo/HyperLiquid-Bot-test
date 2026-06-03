# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T02:22:23.062483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.38` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0006` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0438` n `12`; crypto_alt avg `-0.2893` n `228`; crypto_major avg `-0.1648` n `8`; equity avg `-0.1534` n `69`; fx avg `0.0049` n `6`; index avg `-0.0109` n `23`; metal avg `0.013` n `18`; unknown avg `-0.2064` n `422`
- 1h: commodity avg `-0.1536` n `12`; crypto_alt avg `-0.3222` n `228`; crypto_major avg `-0.4279` n `8`; equity avg `-0.1683` n `69`; fx avg `-0.0161` n `6`; index avg `0.0079` n `23`; metal avg `0.0974` n `18`; unknown avg `-0.1056` n `422`
- 4h: commodity avg `0.1867` n `12`; crypto_alt avg `-0.5551` n `228`; crypto_major avg `-0.7438` n `8`; equity avg `-0.5163` n `69`; fx avg `0.0076` n `6`; index avg `0.2568` n `23`; metal avg `-0.3855` n `18`; unknown avg `-0.7156` n `422`
- 24h: commodity avg `0.6199` n `12`; crypto_alt avg `-3.3248` n `228`; crypto_major avg `-5.3218` n `8`; equity avg `1.5557` n `69`; fx avg `0.0389` n `6`; index avg `1.5873` n `23`; metal avg `-0.058` n `18`; unknown avg `-1.1399` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
