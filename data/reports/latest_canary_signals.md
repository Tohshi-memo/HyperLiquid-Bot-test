# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T12:07:52.143563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0648` n `12`; crypto_alt avg `0.013` n `230`; crypto_major avg `-0.0451` n `8`; equity avg `-0.0522` n `94`; fx avg `0.0309` n `6`; index avg `0.0054` n `25`; metal avg `0.0624` n `20`; unknown avg `0.3697` n `768`
- 1h: commodity avg `0.1831` n `12`; crypto_alt avg `-0.0131` n `230`; crypto_major avg `0.0216` n `8`; equity avg `-0.301` n `94`; fx avg `0.0432` n `6`; index avg `-0.0751` n `25`; metal avg `0.0437` n `20`; unknown avg `0.3206` n `768`
- 4h: commodity avg `0.2078` n `12`; crypto_alt avg `-0.1817` n `230`; crypto_major avg `-0.2837` n `8`; equity avg `-0.6037` n `94`; fx avg `0.0078` n `6`; index avg `-0.1011` n `25`; metal avg `-0.0073` n `20`; unknown avg `0.1259` n `762`
- 24h: commodity avg `0.1426` n `12`; crypto_alt avg `-0.8139` n `230`; crypto_major avg `-0.9416` n `8`; equity avg `-3.2108` n `93`; fx avg `0.0517` n `6`; index avg `-0.5464` n `25`; metal avg `0.0014` n `20`; unknown avg `0.1714` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
