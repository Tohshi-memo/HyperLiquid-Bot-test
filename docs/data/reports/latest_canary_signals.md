# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T00:07:30.513287+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.0532` n `231`; crypto_major avg `-0.1054` n `8`; equity avg `-0.0137` n `128`; fx avg `0.0086` n `6`; index avg `0.0054` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.0355` n `793`
- 1h: commodity avg `-0.0216` n `12`; crypto_alt avg `0.0003` n `231`; crypto_major avg `-0.0501` n `8`; equity avg `0.0016` n `128`; fx avg `0.0168` n `6`; index avg `0.0068` n `26`; metal avg `0.0026` n `20`; unknown avg `0.0619` n `793`
- 4h: commodity avg `-0.009` n `12`; crypto_alt avg `-0.06` n `231`; crypto_major avg `-0.0449` n `8`; equity avg `0.054` n `128`; fx avg `0.0182` n `6`; index avg `0.0036` n `26`; metal avg `0.0108` n `20`; unknown avg `-0.0707` n `774`
- 24h: commodity avg `-0.0043` n `12`; crypto_alt avg `0.1375` n `231`; crypto_major avg `0.6337` n `8`; equity avg `0.3775` n `128`; fx avg `-0.001` n `6`; index avg `0.0836` n `26`; metal avg `0.0892` n `20`; unknown avg `0.2471` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2152`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
