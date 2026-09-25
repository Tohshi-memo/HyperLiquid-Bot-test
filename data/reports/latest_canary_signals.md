# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T14:07:29.658795+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.1928` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.071` n `12`; crypto_alt avg `-0.6206` n `234`; crypto_major avg `-0.3535` n `8`; equity avg `-0.3938` n `141`; fx avg `0.0188` n `6`; index avg `-0.0634` n `26`; metal avg `-0.1743` n `20`; unknown avg `5.803` n `922`
- 1h: commodity avg `0.0` n `12`; crypto_alt avg `-1.5823` n `234`; crypto_major avg `-1.2782` n `8`; equity avg `-1.0446` n `141`; fx avg `-0.0306` n `6`; index avg `-0.0854` n `26`; metal avg `-0.2639` n `20`; unknown avg `120.4815` n `922`
- 4h: commodity avg `-0.0379` n `12`; crypto_alt avg `-0.3403` n `234`; crypto_major avg `-0.0451` n `8`; equity avg `-0.9714` n `141`; fx avg `-0.0387` n `6`; index avg `-0.0908` n `26`; metal avg `-0.2784` n `20`; unknown avg `11.5199` n `916`
- 24h: commodity avg `0.0421` n `12`; crypto_alt avg `1.9845` n `234`; crypto_major avg `1.0339` n `8`; equity avg `0.3707` n `141`; fx avg `-0.232` n `6`; index avg `0.1225` n `26`; metal avg `-0.1087` n `20`; unknown avg `14.2609` n `801`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
