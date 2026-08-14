# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T01:22:27.526377+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0182` n `12`; crypto_alt avg `-0.0392` n `230`; crypto_major avg `-0.0207` n `8`; equity avg `-0.0281` n `113`; fx avg `-0.003` n `6`; index avg `-0.0019` n `25`; metal avg `0.0025` n `20`; unknown avg `-0.0229` n `787`
- 1h: commodity avg `0.0366` n `12`; crypto_alt avg `-0.1436` n `230`; crypto_major avg `0.0035` n `8`; equity avg `-0.2206` n `113`; fx avg `-0.019` n `6`; index avg `-0.0664` n `25`; metal avg `-0.1514` n `20`; unknown avg `-0.0715` n `787`
- 4h: commodity avg `0.0497` n `12`; crypto_alt avg `0.0846` n `230`; crypto_major avg `0.0345` n `8`; equity avg `-0.247` n `113`; fx avg `-0.0197` n `6`; index avg `-0.0553` n `25`; metal avg `-0.2006` n `20`; unknown avg `0.777` n `787`
- 24h: commodity avg `-0.2706` n `12`; crypto_alt avg `0.2709` n `230`; crypto_major avg `0.5538` n `8`; equity avg `1.0989` n `113`; fx avg `0.0513` n `6`; index avg `0.2338` n `25`; metal avg `-0.7138` n `20`; unknown avg `1.1515` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2432`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.207`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.197`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1634`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
