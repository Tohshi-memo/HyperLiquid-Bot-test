# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T04:07:26.226123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0101` n `13`; crypto_alt avg `-0.0578` n `235`; crypto_major avg `-0.0062` n `8`; equity avg `0.013` n `150`; fx avg `-0.0106` n `6`; index avg `-0.0019` n `26`; metal avg `0.015` n `20`; unknown avg `0.1709` n `1069`
- 1h: commodity avg `0.0095` n `13`; crypto_alt avg `-0.1243` n `235`; crypto_major avg `-0.1831` n `8`; equity avg `-0.3199` n `150`; fx avg `-0.0163` n `6`; index avg `-0.0634` n `26`; metal avg `0.0154` n `20`; unknown avg `0.423` n `1069`
- 4h: commodity avg `0.1834` n `13`; crypto_alt avg `-0.2948` n `235`; crypto_major avg `-0.4292` n `8`; equity avg `-0.6982` n `150`; fx avg `0.0149` n `6`; index avg `-0.1116` n `26`; metal avg `0.3577` n `20`; unknown avg `-0.218` n `1069`
- 24h: commodity avg `0.4003` n `13`; crypto_alt avg `-0.4873` n `235`; crypto_major avg `-1.6025` n `8`; equity avg `-1.4794` n `150`; fx avg `-0.1494` n `6`; index avg `-0.2708` n `26`; metal avg `-0.1787` n `20`; unknown avg `247.2137` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
