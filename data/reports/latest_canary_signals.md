# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T18:22:32.683946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.2` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0266` n `12`; crypto_alt avg `-0.2764` n `230`; crypto_major avg `-0.2603` n `8`; equity avg `-0.568` n `102`; fx avg `0.0033` n `6`; index avg `-0.0816` n `25`; metal avg `-0.0565` n `20`; unknown avg `-0.3111` n `778`
- 1h: commodity avg `0.0397` n `12`; crypto_alt avg `0.6003` n `230`; crypto_major avg `0.5057` n `8`; equity avg `0.1855` n `102`; fx avg `0.0173` n `6`; index avg `0.0369` n `25`; metal avg `0.1826` n `20`; unknown avg `-0.2157` n `778`
- 4h: commodity avg `0.1607` n `12`; crypto_alt avg `0.2606` n `230`; crypto_major avg `0.2343` n `8`; equity avg `-0.1433` n `102`; fx avg `-0.0011` n `6`; index avg `0.0146` n `25`; metal avg `0.4551` n `20`; unknown avg `-0.2989` n `778`
- 24h: commodity avg `1.3189` n `12`; crypto_alt avg `-1.3875` n `230`; crypto_major avg `0.4634` n `8`; equity avg `-0.9766` n `102`; fx avg `-0.0276` n `6`; index avg `-0.2326` n `25`; metal avg `0.279` n `20`; unknown avg `-0.6065` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
