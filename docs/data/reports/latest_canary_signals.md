# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T15:22:28.058780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0348` n `12`; crypto_alt avg `0.2094` n `230`; crypto_major avg `0.253` n `8`; equity avg `0.076` n `102`; fx avg `-0.0107` n `6`; index avg `-0.0194` n `25`; metal avg `0.0508` n `20`; unknown avg `0.1422` n `774`
- 1h: commodity avg `-0.1578` n `12`; crypto_alt avg `-0.7014` n `230`; crypto_major avg `-0.5955` n `8`; equity avg `-0.4117` n `102`; fx avg `-0.0374` n `6`; index avg `-0.114` n `25`; metal avg `0.0872` n `20`; unknown avg `-0.0979` n `774`
- 4h: commodity avg `-0.0235` n `12`; crypto_alt avg `-1.5403` n `230`; crypto_major avg `-1.3947` n `8`; equity avg `-2.6043` n `102`; fx avg `-0.0617` n `6`; index avg `-0.5105` n `25`; metal avg `-0.0948` n `20`; unknown avg `0.0656` n `774`
- 24h: commodity avg `-0.595` n `12`; crypto_alt avg `-1.0645` n `230`; crypto_major avg `-0.4854` n `8`; equity avg `-1.7018` n `102`; fx avg `0.0257` n `6`; index avg `-0.4069` n `25`; metal avg `0.2651` n `20`; unknown avg `-0.2304` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1919`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
