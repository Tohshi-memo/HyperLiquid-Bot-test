# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T23:52:28.298784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0142` n `12`; crypto_alt avg `0.0499` n `230`; crypto_major avg `0.0903` n `8`; equity avg `0.0509` n `114`; fx avg `0.0053` n `6`; index avg `0.0147` n `25`; metal avg `0.0087` n `20`; unknown avg `-0.0246` n `792`
- 1h: commodity avg `-0.0109` n `12`; crypto_alt avg `0.1226` n `230`; crypto_major avg `0.1185` n `8`; equity avg `0.0399` n `114`; fx avg `0.0039` n `6`; index avg `0.0122` n `25`; metal avg `-0.0927` n `20`; unknown avg `0.0668` n `791`
- 4h: commodity avg `-0.1357` n `12`; crypto_alt avg `-0.7686` n `230`; crypto_major avg `-0.5414` n `8`; equity avg `0.0323` n `114`; fx avg `0.0078` n `6`; index avg `0.0299` n `25`; metal avg `-0.0451` n `20`; unknown avg `0.4783` n `791`
- 24h: commodity avg `-0.0837` n `12`; crypto_alt avg `-0.605` n `230`; crypto_major avg `-0.3433` n `8`; equity avg `0.2984` n `114`; fx avg `-0.0068` n `6`; index avg `0.0609` n `25`; metal avg `0.0104` n `20`; unknown avg `-0.0441` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1695`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
