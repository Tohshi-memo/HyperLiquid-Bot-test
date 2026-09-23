# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T10:52:38.495573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.234` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0219` n `12`; crypto_alt avg `0.0828` n `234`; crypto_major avg `-0.0058` n `8`; equity avg `-0.0171` n `140`; fx avg `0.0011` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0215` n `20`; unknown avg `0.833` n `946`
- 1h: commodity avg `-0.0271` n `12`; crypto_alt avg `-0.0082` n `234`; crypto_major avg `0.0367` n `8`; equity avg `0.0174` n `140`; fx avg `0.006` n `6`; index avg `-0.0033` n `26`; metal avg `-0.0051` n `20`; unknown avg `1.5917` n `943`
- 4h: commodity avg `0.2165` n `12`; crypto_alt avg `-0.6602` n `234`; crypto_major avg `-1.304` n `8`; equity avg `-0.2062` n `140`; fx avg `0.013` n `6`; index avg `-0.07` n `26`; metal avg `-0.2403` n `20`; unknown avg `1.8547` n `937`
- 24h: commodity avg `0.7712` n `12`; crypto_alt avg `3.9273` n `234`; crypto_major avg `0.6981` n `8`; equity avg `0.7013` n `140`; fx avg `0.0135` n `6`; index avg `0.0306` n `26`; metal avg `-0.1752` n `20`; unknown avg `0.1205` n `842`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.2049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
