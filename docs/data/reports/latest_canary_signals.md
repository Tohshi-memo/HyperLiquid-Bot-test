# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T02:22:32.404415+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0815` n `13`; crypto_alt avg `-0.0472` n `235`; crypto_major avg `-0.0038` n `8`; equity avg `-0.0002` n `151`; fx avg `0.0135` n `6`; index avg `-0.0033` n `26`; metal avg `0.0237` n `20`; unknown avg `0.1855` n `1135`
- 1h: commodity avg `-0.1092` n `13`; crypto_alt avg `0.1739` n `235`; crypto_major avg `0.1039` n `8`; equity avg `0.2218` n `151`; fx avg `-0.0258` n `6`; index avg `0.0669` n `26`; metal avg `0.1136` n `20`; unknown avg `-0.0212` n `1133`
- 4h: commodity avg `0.0572` n `13`; crypto_alt avg `0.3914` n `235`; crypto_major avg `0.2444` n `8`; equity avg `0.0927` n `151`; fx avg `0.001` n `6`; index avg `0.0426` n `26`; metal avg `0.0233` n `20`; unknown avg `0.0532` n `1127`
- 24h: commodity avg `0.9801` n `13`; crypto_alt avg `1.1295` n `235`; crypto_major avg `0.8895` n `8`; equity avg `0.9497` n `151`; fx avg `0.1027` n `6`; index avg `0.1868` n `26`; metal avg `-0.1809` n `20`; unknown avg `1.0622` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1539`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1389`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1094`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.092`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
