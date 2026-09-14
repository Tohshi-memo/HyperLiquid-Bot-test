# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T23:22:32.175368+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.045` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0456` n `12`; crypto_alt avg `-0.0099` n `233`; crypto_major avg `-0.0178` n `8`; equity avg `-0.024` n `136`; fx avg `-0.0001` n `6`; index avg `0.0098` n `27`; metal avg `-0.0285` n `20`; unknown avg `0.8281` n `908`
- 1h: commodity avg `0.0393` n `12`; crypto_alt avg `-0.2166` n `233`; crypto_major avg `-0.4076` n `8`; equity avg `0.0118` n `136`; fx avg `-0.0155` n `6`; index avg `0.0097` n `27`; metal avg `-0.0433` n `20`; unknown avg `1.1568` n `906`
- 4h: commodity avg `0.1505` n `12`; crypto_alt avg `-0.852` n `233`; crypto_major avg `-1.0887` n `8`; equity avg `-0.1475` n `136`; fx avg `-0.009` n `6`; index avg `-0.0437` n `27`; metal avg `-0.0736` n `20`; unknown avg `1.5769` n `866`
- 24h: commodity avg `-0.0861` n `12`; crypto_alt avg `1.3906` n `233`; crypto_major avg `2.5082` n `8`; equity avg `-0.1956` n `136`; fx avg `0.0096` n `6`; index avg `-0.1514` n `27`; metal avg `-0.3726` n `20`; unknown avg `0.5882` n `676`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
