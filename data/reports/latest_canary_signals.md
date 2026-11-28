# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T05:52:28.325916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1387` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0062` n `13`; crypto_alt avg `-0.329` n `239`; crypto_major avg `-0.1158` n `8`; equity avg `-0.0569` n `168`; fx avg `0.0006` n `6`; index avg `-0.0027` n `27`; metal avg `-0.0067` n `20`; unknown avg `0.2921` n `1267`
- 1h: commodity avg `-0.0008` n `13`; crypto_alt avg `-1.2374` n `239`; crypto_major avg `-0.6179` n `8`; equity avg `-0.3216` n `168`; fx avg `-0.0086` n `6`; index avg `-0.0284` n `27`; metal avg `-0.0399` n `20`; unknown avg `2.9571` n `1255`
- 4h: commodity avg `0.0305` n `13`; crypto_alt avg `-2.2869` n `239`; crypto_major avg `-1.1653` n `8`; equity avg `-0.1685` n `168`; fx avg `0.0018` n `6`; index avg `-0.0266` n `27`; metal avg `-0.017` n `20`; unknown avg `0.1855` n `1241`
- 24h: commodity avg `-0.8519` n `13`; crypto_alt avg `-3.2755` n `239`; crypto_major avg `-2.7348` n `8`; equity avg `-0.5076` n `168`; fx avg `-0.1456` n `6`; index avg `-0.0095` n `27`; metal avg `-0.1531` n `20`; unknown avg `214.776` n `975`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
