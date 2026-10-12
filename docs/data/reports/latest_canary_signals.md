# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T05:07:32.464025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0309` n `13`; crypto_alt avg `0.2839` n `235`; crypto_major avg `0.1374` n `8`; equity avg `-0.0673` n `151`; fx avg `-0.0003` n `6`; index avg `-0.0124` n `26`; metal avg `-0.0244` n `20`; unknown avg `1.0087` n `1131`
- 1h: commodity avg `0.0102` n `13`; crypto_alt avg `0.9847` n `235`; crypto_major avg `0.8597` n `8`; equity avg `0.0604` n `151`; fx avg `0.0155` n `6`; index avg `-0.0081` n `26`; metal avg `-0.0424` n `20`; unknown avg `1.1706` n `1077`
- 4h: commodity avg `0.0288` n `13`; crypto_alt avg `0.972` n `235`; crypto_major avg `0.7286` n `8`; equity avg `-0.6583` n `151`; fx avg `0.0116` n `6`; index avg `-0.0186` n `26`; metal avg `-0.0615` n `20`; unknown avg `0.3135` n `1051`
- 24h: commodity avg `-0.4706` n `13`; crypto_alt avg `3.3888` n `235`; crypto_major avg `1.9502` n `8`; equity avg `-0.2076` n `151`; fx avg `-0.0506` n `6`; index avg `0.0109` n `26`; metal avg `0.0995` n `20`; unknown avg `1.1865` n `874`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
