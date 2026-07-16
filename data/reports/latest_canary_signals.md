# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T00:22:26.321190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0` n `5`; crypto_alt avg `-0.0023` n `230`; crypto_major avg `-0.1469` n `8`; equity avg `-0.0165` n `20`; fx avg `0.0` n `1`; index avg `0.0005` n `19`; metal avg `0.0049` n `14`; unknown avg `-0.0382` n `764`
- 1h: commodity avg `-0.0755` n `12`; crypto_alt avg `-0.0801` n `230`; crypto_major avg `-0.2498` n `8`; equity avg `-0.2862` n `94`; fx avg `0.0078` n `6`; index avg `-0.0689` n `25`; metal avg `0.0139` n `20`; unknown avg `0.0796` n `766`
- 4h: commodity avg `-0.1343` n `12`; crypto_alt avg `-0.1181` n `230`; crypto_major avg `-0.2207` n `8`; equity avg `-0.3622` n `94`; fx avg `-0.0093` n `6`; index avg `-0.0749` n `25`; metal avg `-0.0033` n `20`; unknown avg `0.3055` n `766`
- 24h: commodity avg `-0.1098` n `12`; crypto_alt avg `0.212` n `230`; crypto_major avg `0.353` n `8`; equity avg `-1.4739` n `93`; fx avg `0.1727` n `6`; index avg `-0.3497` n `25`; metal avg `0.1078` n `20`; unknown avg `0.092` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
