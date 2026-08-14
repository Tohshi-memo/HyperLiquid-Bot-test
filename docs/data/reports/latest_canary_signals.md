# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T16:22:31.762891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0119` n `12`; crypto_alt avg `0.1183` n `230`; crypto_major avg `0.0574` n `8`; equity avg `0.1225` n `114`; fx avg `-0.002` n `6`; index avg `0.0101` n `25`; metal avg `0.0229` n `20`; unknown avg `0.0348` n `791`
- 1h: commodity avg `-0.037` n `12`; crypto_alt avg `0.7766` n `230`; crypto_major avg `0.3122` n `8`; equity avg `0.0992` n `114`; fx avg `0.0441` n `6`; index avg `-0.0134` n `25`; metal avg `0.081` n `20`; unknown avg `0.1703` n `791`
- 4h: commodity avg `-0.0025` n `12`; crypto_alt avg `0.7301` n `230`; crypto_major avg `0.2161` n `8`; equity avg `-0.5797` n `114`; fx avg `0.114` n `6`; index avg `-0.1269` n `25`; metal avg `0.0937` n `20`; unknown avg `-0.2011` n `786`
- 24h: commodity avg `-0.0859` n `12`; crypto_alt avg `0.1514` n `230`; crypto_major avg `-0.6751` n `8`; equity avg `-0.2974` n `114`; fx avg `0.0951` n `6`; index avg `-0.0673` n `25`; metal avg `0.2641` n `20`; unknown avg `0.3726` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1815`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1648`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
