# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T08:07:18.567356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1257` n `12`; crypto_alt avg `0.2991` n `228`; crypto_major avg `0.1514` n `8`; equity avg `0.2407` n `66`; fx avg `-0.0049` n `5`; index avg `0.1048` n `23`; metal avg `0.1029` n `18`; unknown avg `0.0621` n `383`
- 1h: commodity avg `-0.2626` n `12`; crypto_alt avg `0.001` n `228`; crypto_major avg `0.0211` n `8`; equity avg `0.2761` n `66`; fx avg `-0.0226` n `5`; index avg `0.0573` n `23`; metal avg `0.0267` n `18`; unknown avg `-0.0392` n `383`
- 4h: commodity avg `-0.325` n `12`; crypto_alt avg `-0.5033` n `228`; crypto_major avg `-0.2819` n `8`; equity avg `0.3939` n `66`; fx avg `-0.0689` n `5`; index avg `0.1273` n `23`; metal avg `0.2867` n `18`; unknown avg `-0.1238` n `363`
- 24h: commodity avg `0.5679` n `12`; crypto_alt avg `-2.8626` n `228`; crypto_major avg `-1.2625` n `8`; equity avg `0.2507` n `65`; fx avg `0.0381` n `5`; index avg `0.2121` n `23`; metal avg `0.0139` n `18`; unknown avg `-0.3887` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
