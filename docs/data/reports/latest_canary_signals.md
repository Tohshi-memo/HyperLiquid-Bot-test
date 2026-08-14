# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T02:07:24.147394+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0103` n `12`; crypto_alt avg `0.0808` n `230`; crypto_major avg `0.0972` n `8`; equity avg `-0.0474` n `113`; fx avg `0.0101` n `6`; index avg `0.0164` n `25`; metal avg `0.0103` n `20`; unknown avg `0.0422` n `787`
- 1h: commodity avg `-0.0846` n `12`; crypto_alt avg `0.1514` n `230`; crypto_major avg `0.0438` n `8`; equity avg `-0.0927` n `113`; fx avg `-0.0277` n `6`; index avg `0.0126` n `25`; metal avg `-0.0307` n `20`; unknown avg `0.0397` n `787`
- 4h: commodity avg `0.0028` n `12`; crypto_alt avg `0.1631` n `230`; crypto_major avg `0.0533` n `8`; equity avg `-0.402` n `113`; fx avg `-0.0424` n `6`; index avg `-0.0477` n `25`; metal avg `-0.1985` n `20`; unknown avg `0.743` n `787`
- 24h: commodity avg `-0.3232` n `12`; crypto_alt avg `0.5393` n `230`; crypto_major avg `0.6241` n `8`; equity avg `0.7604` n `113`; fx avg `0.0094` n `6`; index avg `0.222` n `25`; metal avg `-0.6693` n `20`; unknown avg `1.2358` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2449`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2079`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.186`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1641`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
