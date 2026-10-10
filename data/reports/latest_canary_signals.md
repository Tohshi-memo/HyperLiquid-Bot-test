# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T21:22:22.117944+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0149` n `13`; crypto_alt avg `-0.0146` n `235`; crypto_major avg `-0.0479` n `8`; equity avg `0.0055` n `150`; fx avg `-0.0017` n `6`; index avg `0.0004` n `26`; metal avg `-0.0042` n `20`; unknown avg `1.0008` n `1117`
- 1h: commodity avg `0.0148` n `13`; crypto_alt avg `0.3033` n `235`; crypto_major avg `0.0882` n `8`; equity avg `0.0322` n `150`; fx avg `-0.0019` n `6`; index avg `0.0076` n `26`; metal avg `0.0063` n `20`; unknown avg `11.467` n `1109`
- 4h: commodity avg `0.0086` n `13`; crypto_alt avg `0.5489` n `235`; crypto_major avg `0.0596` n `8`; equity avg `0.0615` n `150`; fx avg `-0.0014` n `6`; index avg `0.0082` n `26`; metal avg `0.0045` n `20`; unknown avg `2.4375` n `993`
- 24h: commodity avg `-0.0995` n `13`; crypto_alt avg `2.8656` n `235`; crypto_major avg `0.929` n `8`; equity avg `0.1956` n `150`; fx avg `-0.0121` n `6`; index avg `0.0174` n `26`; metal avg `-0.0153` n `20`; unknown avg `2.285` n `966`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
