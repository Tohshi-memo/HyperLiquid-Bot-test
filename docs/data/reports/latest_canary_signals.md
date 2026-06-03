# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T00:06:32.811224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.37` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.6572` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.644` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1412` n `12`; crypto_alt avg `0.2495` n `228`; crypto_major avg `0.1686` n `8`; equity avg `0.1752` n `69`; fx avg `0.0147` n `6`; index avg `0.0622` n `23`; metal avg `0.1094` n `18`; unknown avg `-0.0265` n `422`
- 1h: commodity avg `-0.0865` n `12`; crypto_alt avg `-0.085` n `228`; crypto_major avg `0.2221` n `8`; equity avg `-0.0555` n `69`; fx avg `-0.0092` n `6`; index avg `0.1197` n `23`; metal avg `0.0339` n `18`; unknown avg `0.9442` n `422`
- 4h: commodity avg `0.2625` n `12`; crypto_alt avg `-1.6935` n `228`; crypto_major avg `-1.5909` n `8`; equity avg `0.0663` n `69`; fx avg `-0.0496` n `6`; index avg `0.0531` n `23`; metal avg `-0.1788` n `18`; unknown avg `0.4395` n `422`
- 24h: commodity avg `0.4492` n `12`; crypto_alt avg `-5.161` n `228`; crypto_major avg `-6.0132` n `8`; equity avg `1.3102` n `69`; fx avg `0.0189` n `6`; index avg `0.9423` n `23`; metal avg `0.2661` n `18`; unknown avg `-0.6199` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
