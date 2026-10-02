# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T14:37:27.104664+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.42` - Polymarket crypto volume is unusually high.
- 1h_crypto_equity_divergence: score `-1.7729` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `-1.6303` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.4806` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.0148` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0569` n `13`; crypto_alt avg `-0.5732` n `235`; crypto_major avg `-0.716` n `8`; equity avg `0.0015` n `143`; fx avg `0.01` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0716` n `20`; unknown avg `1.1636` n `962`
- 1h: commodity avg `-0.0721` n `13`; crypto_alt avg `-0.9732` n `235`; crypto_major avg `-1.4161` n `8`; equity avg `0.3568` n `143`; fx avg `0.0537` n `6`; index avg `0.0645` n `26`; metal avg `-0.1303` n `20`; unknown avg `2.3961` n `942`
- 4h: commodity avg `-0.0571` n `13`; crypto_alt avg `0.1255` n `235`; crypto_major avg `-0.7783` n `8`; equity avg `0.852` n `142`; fx avg `0.0483` n `6`; index avg `0.2365` n `26`; metal avg `-0.0189` n `20`; unknown avg `1.4314` n `936`
- 24h: commodity avg `-0.739` n `13`; crypto_alt avg `2.4779` n `235`; crypto_major avg `1.3225` n `8`; equity avg `2.4755` n `142`; fx avg `-0.1916` n `6`; index avg `0.5999` n `26`; metal avg `-0.003` n `20`; unknown avg `105.352` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1702`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
