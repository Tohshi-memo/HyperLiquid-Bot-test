# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T01:07:28.398183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `-0.0754` n `230`; crypto_major avg `0.0271` n `8`; equity avg `0.004` n `114`; fx avg `0.0005` n `6`; index avg `0.0022` n `25`; metal avg `0.0031` n `20`; unknown avg `-0.0002` n `791`
- 1h: commodity avg `0.0112` n `12`; crypto_alt avg `-0.0415` n `230`; crypto_major avg `0.0507` n `8`; equity avg `-0.0285` n `114`; fx avg `0.0015` n `6`; index avg `-0.001` n `25`; metal avg `0.0071` n `20`; unknown avg `-0.0565` n `791`
- 4h: commodity avg `0.0046` n `12`; crypto_alt avg `-0.4244` n `230`; crypto_major avg `-0.1894` n `8`; equity avg `-0.0109` n `114`; fx avg `-0.0006` n `6`; index avg `0.0172` n `25`; metal avg `0.0055` n `20`; unknown avg `-0.1179` n `791`
- 24h: commodity avg `-0.0766` n `12`; crypto_alt avg `0.1209` n `230`; crypto_major avg `0.1339` n `8`; equity avg `0.1767` n `114`; fx avg `0.0342` n `6`; index avg `0.0138` n `25`; metal avg `-0.0439` n `20`; unknown avg `-0.0189` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2246`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.171`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
