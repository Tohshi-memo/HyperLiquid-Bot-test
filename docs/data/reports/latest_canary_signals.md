# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T21:11:28.687957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `5.08` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0737` n `12`; crypto_alt avg `0.0661` n `230`; crypto_major avg `0.1732` n `8`; equity avg `0.0116` n `92`; fx avg `-0.0005` n `6`; index avg `-0.0007` n `25`; metal avg `0.0169` n `20`; unknown avg `-0.4291` n `768`
- 1h: commodity avg `-0.0852` n `12`; crypto_alt avg `0.0767` n `230`; crypto_major avg `0.1698` n `8`; equity avg `0.0347` n `92`; fx avg `0.0086` n `6`; index avg `-0.0063` n `25`; metal avg `-0.0345` n `20`; unknown avg `-0.2037` n `768`
- 4h: commodity avg `0.0969` n `12`; crypto_alt avg `-0.2587` n `230`; crypto_major avg `0.3333` n `8`; equity avg `0.2131` n `92`; fx avg `-0.0044` n `6`; index avg `-0.0125` n `25`; metal avg `-0.0115` n `20`; unknown avg `-0.04` n `766`
- 24h: commodity avg `0.291` n `12`; crypto_alt avg `1.9185` n `230`; crypto_major avg `3.5582` n `8`; equity avg `1.3874` n `92`; fx avg `-0.0005` n `6`; index avg `0.422` n `25`; metal avg `0.5711` n `20`; unknown avg `0.1783` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1756`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
