# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T05:37:28.574901+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3337` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0207` n `13`; crypto_alt avg `0.1524` n `235`; crypto_major avg `0.0558` n `8`; equity avg `0.0933` n `150`; fx avg `-0.0065` n `6`; index avg `0.0109` n `26`; metal avg `0.0218` n `20`; unknown avg `-0.1226` n `1076`
- 1h: commodity avg `0.008` n `13`; crypto_alt avg `0.5799` n `235`; crypto_major avg `0.3853` n `8`; equity avg `-0.0504` n `150`; fx avg `-0.0082` n `6`; index avg `-0.0108` n `26`; metal avg `-0.0524` n `20`; unknown avg `0.3124` n `1074`
- 4h: commodity avg `0.0638` n `13`; crypto_alt avg `-2.3274` n `235`; crypto_major avg `-1.3875` n `8`; equity avg `-0.3251` n `150`; fx avg `-0.0414` n `6`; index avg `-0.0538` n `26`; metal avg `-0.2042` n `20`; unknown avg `1.2862` n `1068`
- 24h: commodity avg `0.5034` n `13`; crypto_alt avg `-3.2712` n `235`; crypto_major avg `-2.2935` n `8`; equity avg `-0.0908` n `149`; fx avg `0.0389` n `6`; index avg `-0.0386` n `26`; metal avg `-0.0597` n `20`; unknown avg `871.6204` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1823`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
