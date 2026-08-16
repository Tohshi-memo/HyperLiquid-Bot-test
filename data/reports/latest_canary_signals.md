# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T14:09:39.375845+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `-0.0187` n `230`; crypto_major avg `-0.0043` n `8`; equity avg `-0.0119` n `114`; fx avg `0.0001` n `6`; index avg `0.0` n `25`; metal avg `0.0089` n `20`; unknown avg `-0.0216` n `791`
- 1h: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.0318` n `230`; crypto_major avg `-0.0099` n `8`; equity avg `0.0234` n `114`; fx avg `-0.0073` n `6`; index avg `0.0055` n `25`; metal avg `0.0042` n `20`; unknown avg `0.0212` n `791`
- 4h: commodity avg `-0.0067` n `12`; crypto_alt avg `0.0496` n `230`; crypto_major avg `0.0533` n `8`; equity avg `-0.097` n `114`; fx avg `-0.0139` n `6`; index avg `0.0067` n `25`; metal avg `-0.0001` n `20`; unknown avg `0.1561` n `791`
- 24h: commodity avg `0.0499` n `12`; crypto_alt avg `0.0673` n `230`; crypto_major avg `0.0581` n `8`; equity avg `0.2269` n `114`; fx avg `-0.0191` n `6`; index avg `0.0396` n `25`; metal avg `0.0393` n `20`; unknown avg `0.1815` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2154`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1646`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
