# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T14:37:28.976561+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.33` - Polymarket crypto volume is unusually high.
- 1h_index_leads_crypto: score `1.027` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0023` n `12`; crypto_alt avg `-0.181` n `234`; crypto_major avg `-0.195` n `8`; equity avg `-0.2993` n `142`; fx avg `0.0371` n `6`; index avg `-0.0598` n `26`; metal avg `-0.1267` n `20`; unknown avg `0.2728` n `963`
- 1h: commodity avg `0.0126` n `12`; crypto_alt avg `-0.7073` n `234`; crypto_major avg `-1.0206` n `8`; equity avg `-0.2158` n `142`; fx avg `0.0168` n `6`; index avg `0.0064` n `26`; metal avg `-0.1565` n `20`; unknown avg `4.3692` n `907`
- 4h: commodity avg `0.1001` n `12`; crypto_alt avg `-0.5073` n `234`; crypto_major avg `-0.5987` n `8`; equity avg `-0.0493` n `142`; fx avg `-0.0183` n `6`; index avg `0.0964` n `26`; metal avg `-0.2161` n `20`; unknown avg `6.9678` n `901`
- 24h: commodity avg `0.0065` n `12`; crypto_alt avg `-1.121` n `234`; crypto_major avg `-1.1489` n `8`; equity avg `-0.7943` n `142`; fx avg `0.0395` n `6`; index avg `0.0623` n `26`; metal avg `-0.0484` n `20`; unknown avg `9197.3964` n `836`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
