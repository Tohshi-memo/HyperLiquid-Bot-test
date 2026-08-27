# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T20:37:26.846376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0178` n `12`; crypto_alt avg `-0.0956` n `231`; crypto_major avg `-0.2107` n `8`; equity avg `-0.0329` n `127`; fx avg `-0.0027` n `6`; index avg `-0.0048` n `26`; metal avg `-0.0255` n `20`; unknown avg `0.0632` n `792`
- 1h: commodity avg `-0.082` n `12`; crypto_alt avg `-0.0045` n `231`; crypto_major avg `-0.1818` n `8`; equity avg `0.1222` n `127`; fx avg `-0.0001` n `6`; index avg `0.0339` n `26`; metal avg `-0.0252` n `20`; unknown avg `0.2099` n `792`
- 4h: commodity avg `0.0826` n `12`; crypto_alt avg `-0.9059` n `231`; crypto_major avg `-0.4017` n `8`; equity avg `0.2925` n `127`; fx avg `0.0086` n `6`; index avg `0.0131` n `26`; metal avg `0.0541` n `20`; unknown avg `0.4076` n `792`
- 24h: commodity avg `0.3871` n `12`; crypto_alt avg `3.3009` n `231`; crypto_major avg `4.2868` n `8`; equity avg `1.2689` n `127`; fx avg `-0.0305` n `6`; index avg `0.1705` n `26`; metal avg `0.2597` n `20`; unknown avg `1.0334` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
