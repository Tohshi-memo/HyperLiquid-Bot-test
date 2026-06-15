# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T23:52:38.029662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0409` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0295` n `12`; crypto_alt avg `0.3815` n `228`; crypto_major avg `0.3328` n `8`; equity avg `0.039` n `77`; fx avg `0.0016` n `6`; index avg `0.108` n `23`; metal avg `-0.0403` n `18`; unknown avg `15.498` n `687`
- 1h: commodity avg `0.1152` n `12`; crypto_alt avg `0.441` n `228`; crypto_major avg `0.0811` n `8`; equity avg `0.0199` n `77`; fx avg `-0.0806` n `6`; index avg `0.0179` n `23`; metal avg `0.0034` n `18`; unknown avg `15.2308` n `687`
- 4h: commodity avg `-0.0004` n `12`; crypto_alt avg `-0.3788` n `228`; crypto_major avg `-1.0172` n `8`; equity avg `-0.0525` n `77`; fx avg `-0.031` n `6`; index avg `0.0237` n `23`; metal avg `-0.1514` n `18`; unknown avg `0.1364` n `679`
- 24h: commodity avg `0.5768` n `12`; crypto_alt avg `0.9697` n `228`; crypto_major avg `2.0944` n `8`; equity avg `1.6876` n `76`; fx avg `-0.0398` n `6`; index avg `1.0617` n `23`; metal avg `0.1355` n `18`; unknown avg `1.6919` n `519`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0466`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0448`, n `668`, weak_sample_signal
