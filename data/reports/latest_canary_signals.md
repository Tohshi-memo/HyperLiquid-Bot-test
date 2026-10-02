# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T17:37:31.474037+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.0492` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.3633` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.9877` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.8774` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0453` n `13`; crypto_alt avg `-0.3124` n `235`; crypto_major avg `-0.1654` n `8`; equity avg `-0.0382` n `143`; fx avg `-0.0019` n `6`; index avg `-0.0177` n `26`; metal avg `-0.006` n `20`; unknown avg `5.1987` n `984`
- 1h: commodity avg `0.3036` n `13`; crypto_alt avg `-0.7467` n `235`; crypto_major avg `-0.3415` n `8`; equity avg `-0.2144` n `143`; fx avg `0.0184` n `6`; index avg `-0.0319` n `26`; metal avg `-0.0087` n `20`; unknown avg `2.2205` n `982`
- 4h: commodity avg `0.5877` n `13`; crypto_alt avg `-2.1959` n `235`; crypto_major avg `-2.4615` n `8`; equity avg `-0.5841` n `143`; fx avg `0.0626` n `6`; index avg `-0.0982` n `26`; metal avg `-0.4738` n `20`; unknown avg `2.6956` n `934`
- 24h: commodity avg `-0.0379` n `13`; crypto_alt avg `0.669` n `235`; crypto_major avg `0.0277` n `8`; equity avg `0.4356` n `142`; fx avg `-0.0639` n `6`; index avg `0.2545` n `26`; metal avg `-0.3588` n `20`; unknown avg `99.5625` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1675`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
