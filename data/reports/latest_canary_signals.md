# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T20:07:32.215661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0193` n `12`; crypto_alt avg `-0.0053` n `230`; crypto_major avg `-0.0456` n `8`; equity avg `-0.0904` n `98`; fx avg `-0.0111` n `6`; index avg `-0.0324` n `25`; metal avg `-0.013` n `20`; unknown avg `-0.0192` n `770`
- 1h: commodity avg `-0.1307` n `12`; crypto_alt avg `-0.0281` n `230`; crypto_major avg `-0.0852` n `8`; equity avg `-0.1653` n `98`; fx avg `-0.0095` n `6`; index avg `-0.0255` n `25`; metal avg `-0.0079` n `20`; unknown avg `-0.1502` n `770`
- 4h: commodity avg `0.2331` n `12`; crypto_alt avg `0.0368` n `230`; crypto_major avg `-0.27` n `8`; equity avg `-1.0724` n `98`; fx avg `-0.0051` n `6`; index avg `-0.2454` n `25`; metal avg `-0.1922` n `20`; unknown avg `-0.223` n `770`
- 24h: commodity avg `-0.3934` n `12`; crypto_alt avg `1.5415` n `230`; crypto_major avg `1.0882` n `8`; equity avg `-0.1958` n `98`; fx avg `-0.2114` n `6`; index avg `0.0336` n `25`; metal avg `0.0741` n `20`; unknown avg `0.1426` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.106`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1052`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0933`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0846`, n `666`, weak_sample_signal
