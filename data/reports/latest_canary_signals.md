# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T00:22:29.758812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.0851` n `228`; crypto_major avg `-0.0816` n `8`; equity avg `-0.3048` n `88`; fx avg `0.0217` n `6`; index avg `-0.0796` n `23`; metal avg `-0.0784` n `20`; unknown avg `0.1983` n `764`
- 1h: commodity avg `-0.076` n `12`; crypto_alt avg `0.0556` n `228`; crypto_major avg `-0.0936` n `8`; equity avg `-0.4857` n `88`; fx avg `0.0405` n `6`; index avg `-0.2182` n `23`; metal avg `-0.1113` n `20`; unknown avg `1.8145` n `764`
- 4h: commodity avg `-0.4711` n `12`; crypto_alt avg `-0.6422` n `228`; crypto_major avg `-0.6356` n `8`; equity avg `-0.4` n `88`; fx avg `-0.0028` n `6`; index avg `-0.1132` n `23`; metal avg `-0.3047` n `20`; unknown avg `0.2564` n `762`
- 24h: commodity avg `-0.4334` n `12`; crypto_alt avg `-0.8601` n `228`; crypto_major avg `-1.0967` n `8`; equity avg `-0.2049` n `88`; fx avg `-0.0339` n `6`; index avg `-0.106` n `23`; metal avg `-0.3356` n `20`; unknown avg `15.5952` n `690`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1882`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
